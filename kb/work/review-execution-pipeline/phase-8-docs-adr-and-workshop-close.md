# Phase 8: Docs, ADR, and workshop close

**Status: planned.** Phase 8 promotes the durable decisions and closes the workshop after the queued-job pipeline behavior has landed.

## Purpose

Turn the implementation into durable reference knowledge and remove workshop scaffolding that should not become a permanent navigation surface.

## Scope

In scope:

- promote [adr-draft-034-queued-review-jobs-and-execution-provenance.md](./adr-draft-034-queued-review-jobs-and-execution-provenance.md) into `kb/reference/adr/` with the next available ADR number;
- adjust the promoted ADR links so it supersedes-in-part ADR 031 and extends ADR 029, ADR 030, ADR 032, and ADR 033;
- update `kb/reference/review-architecture.md`;
- update command reference docs;
- update operator docs and review-system docs;
- remove command wrappers that survived only as temporary bridges;
- remove or archive obsolete workshop files;
- close the workshop by promoting durable artifacts and deleting the work folder if no active design remains.

Out of scope:

- changing implementation behavior;
- adding new queue features;
- adopting the model partition registry proposal;
- adopting the content-hash/event-log source-of-truth alternative.

## ADR handling

The ADR decision text lives in [adr-draft-034-queued-review-jobs-and-execution-provenance.md](./adr-draft-034-queued-review-jobs-and-execution-provenance.md). Phase 8 should move that draft into the reference collection after implementation, update relative links/frontmatter/status, and avoid duplicating ADR content in the phase plan.

## Tests and validation

- full `pytest`;
- `commonplace-validate` on updated docs;
- command reference examples match actual CLI flags;
- no live docs describe removed command surfaces as current;
- workshop README points only to remaining active work, or the workshop is deleted.

## Done when

Phase 8 is done when the shipped system is described in durable reference docs and ADRs, old command surfaces are no longer documented as current, and the workshop has either closed or been reduced to explicitly remaining future work.
