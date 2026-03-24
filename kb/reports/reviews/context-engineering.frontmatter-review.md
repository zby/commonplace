<!-- REVIEW-METADATA
note-path: kb/notes/context-engineering.md
last-full-review-note-sha: a2297b307ec3efda1379da39140b48e8d32a2d21
last-full-review-note-commit: 0c513b55663f04adfe75e1e5664b3f5eff7b0bed
last-full-review-at: 2026-03-24T20:54:16+01:00
last-accepted-note-sha: a2297b307ec3efda1379da39140b48e8d32a2d21
last-accepted-note-commit: 0c513b55663f04adfe75e1e5664b3f5eff7b0bed
last-accepted-at: 2026-03-24T20:54:16+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: context-engineering.md ===

Checks applied: 4

WARN:
- [Title composability] Title "Context engineering" is a bare topic noun phrase. "since context engineering..." does not complete as a sentence fragment. However, this is a definitional/term-pinning note (description opens with "Definition --", status is seedling), which is an accepted exception for topical titles per claim-strength exceptions. Escalating to WARN rather than CLEAN because the composability test itself does not list definitional notes as an exception -- only the claim-strength check does.
  Recommendation: If composability matters more than the definitional signal, consider a claim-form title like "context engineering is the discipline of designing systems around bounded-context constraints." Otherwise, acknowledge the topical title is intentional for term pinning and leave as-is.

INFO:
- [Description discrimination] Description begins with the label "Definition --" which is a useful genre signal but consumes ~14 characters of the budget. The substantive content that follows ("context engineering is the discipline of designing systems around bounded-context constraints; its operational core is routing, loading, scoping, and maintenance for each bounded call") adds mechanism (four-component decomposition) and scope (bounded-context constraints). This discriminates well against other notes that merely reference context engineering. The "Definition" prefix helps an agent identify this as the canonical definitional entry. No action needed, but worth noting the prefix is a convention choice rather than a retrieval necessity.

CLEAN:
- [Description discrimination] The description adds mechanism (the four operational components: routing, loading, scoping, maintenance) and scope (bounded-context constraints) beyond what the bare topic title carries. An agent searching for "context engineering" among multiple results would identify this as the definitional overview note. Passes.
- [Claim strength] The title is not phrased as a claim -- it is a bare topic label. The note is definitional (term pinning) with status "seedling," which is an explicit exception. Topical titles are correct for definitional notes. Passes.
- [Title-body alignment] The title promises an overview of "context engineering." The body delivers a definition, a four-component operational decomposition (routing, loading, scoping, maintenance), and an architectural scope section covering storage format, knowledge lifecycle, session boundaries, inter-agent communication, and tool/interface design. Title and body are aligned. Passes.

Overall: 1 warning, 1 info
===
