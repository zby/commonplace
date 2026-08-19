# S1 plan — Name the snapshot's mutable envelope

**State:** open. The ingest skill now acknowledges that a run may have edited a
snapshot during validation, but no step authorizes the edit and its final
constraint still forbids it.

## Resolution selected

Replace whole-file immutability with **captured-content immutability**. After
capture, the body, source identity, capture provenance, and authored-link
surface do not change. Ingestion may correct exactly the snapshot frontmatter
`genre` field when closer reading disproves the capture-time classification.
Capture cleanup remains part of initial capture, not a later general mutation
right. Any other later mutation is refused and reported as requiring a
separately authorized workflow that does not exist yet.

## Work

1. Tighten ADR 045's Decision and Consequences so the one-field exception and
   the immutable remainder are stated together.
2. Rewrite both categorical passages in `kb/sources/COLLECTION.md`. The fidelity
   section should distinguish captured content from correctable classification;
   the outbound section should say that no links or annotations are authored
   into the captured body.
3. Align the snapshot and ingest-report type specs on the same terms. Preserve
   the snapshot as the single authoritative genre record and keep the report's
   Classification prose as justification, not a second field.
4. Update `cp-skill-ingest` to:
   - authorize direct writes to the report plus the narrow snapshot correction;
   - load the resolved snapshot type and read the current `genre`;
   - compare it with the classification reached by closer reading;
   - when they differ, edit only the `genre` scalar before drafting the report;
   - validate both changed artifacts and report old/new genre values only in
     the final user response; the durable report records only the corrected
     current genre in its Classification prose.
5. Qualify `cp-skill-connect`'s remaining statement that snapshots are
   immutable so it means body and authored-link immutability, not a prohibition
   on the ADR-authorized metadata correction.
6. Carry the same wording into the installed sources template created by I3.

## Acceptance

- With a correct capture-time classification, ingest creates the report and the
  snapshot remains byte-identical.
- With a wrong classification, the snapshot diff changes only the `genre`
  scalar value; every other byte, including the body and every other
  frontmatter field, remains identical.
- Both artifacts validate, and the report names the corrected genre without
  storing a duplicate frontmatter field.
- A requested change to any other snapshot part is refused and the response
  states that it needs a separately authorized recapture/correction workflow.

S1 closes when the collection, ADR, both types, ingest, connect, and installed
template all authorize exactly the same write boundary.
