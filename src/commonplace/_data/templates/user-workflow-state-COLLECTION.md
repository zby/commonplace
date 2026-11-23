---
type: types/collection-contract.md
description: "Workflow-owned records used to continue a run, inspect a result, or recover an earlier decision; not the retained reports a clean checkout can cite."
---

# Workflow state

## Purpose

Use this collection to answer questions such as “Why did this run stop?” or “Which finding did the operator already decide?” A record belongs here when a named workflow owns it and reads it or keeps it to explain its work. Completion does not make the record disposable. Put an exact report readers need in a clean checkout in `kb/reports/retained/`; put an unfinished investigation in `kb/work/`.

## Layout and maintenance

The main repository owns this contract and the landing. New workflow payloads belong under `data/current/`, one directory per producing workflow. Older records beside `current/` are historical evidence, not inputs to current commands. Keep embedded paths in those records unchanged. The whole payload tree can be a separate checkout. A main-repository clone need not contain it.

Keep the identifiers, paths and evidence the owning workflow uses. Follow its filename, title and description conventions; do not rename a generated record for readability. Attribute inputs and judgments as required by the workflow. Staged candidates retain their destination format; keep exact captures unchanged. The state repository's README identifies what deletion loses for each workflow. Only the owning workflow sets the cleanup rule.

## Outbound links

A record may point inline to any KB collection to identify its inputs, outputs or governing procedure, or to an external source when the workflow records it as evidence. Keep references used by the workflow resolvable. Do not add formal footer links or topic tags to run records for discovery. Tags and links in an exact capture describe the captured artifact, not this collection.
