# Verification

Source and consistency review by the authoring agent on 2026-09-19; neither
independent review nor experimental reproduction. Checked the primary Popper
passages, modern-paper claims and limits, source identities, and migration
targets. The resulting distinctions are incorporated in the candidate and
comparison. The full-text access search was not repeated during verification.

Before compression, 30 of 31 artifacts passed validation: six workshop files,
the index, six ingests, six snapshots, and twelve connection reports. The
sole failure was `validation.schema.body-dates-1`: İşcan's bibliography DOI
`10.1186/1471-2288-13-91` is misread as containing a date. Snapshot bytes remain
unchanged. All six snapshot checksums, required empty Quotes blocks, relative
file links, and workshop heading anchors passed.

After compression, all seven workshop files validate and their file links and
heading anchors resolve. Sources, article, library definitions, and peer
workshops were unchanged by this cleanup. Source coverage limits remain in
[sources](./sources.md); unresolved conceptual choices remain in the
[candidate](./candidate-ontology.md#choices-before-promotion).
