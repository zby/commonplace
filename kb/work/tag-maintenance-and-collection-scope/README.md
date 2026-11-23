# Tag maintenance and collection scope

Posed by the operator on 2026-11-23. Make tag maintenance usable again, run it against the existing KB, and make tracked sources routinely findable by topic. Decide whether other collections should use tags. A long interval since the last audit is a reason to inspect the structure, not evidence that a particular tag needs changing.

The [search-command ledger](./search-command-ledger.md) records which instructions search by topic, which require exact membership, and which must keep a wider scope to find dependencies.

## Where the work starts

- The [search checks](./search-checks.md) verified the corrected [maintenance instruction](../../instructions/maintain-curated-indexes.md) against the [tag contract](../../tags/COLLECTION.md). Use it next to assess heads, assignments and eligible but untagged material. A passing validator cannot tell whether a head helps a writer distinguish two neighboring topics.
- [Tracked source analyses](../../sources/COLLECTION.md#topic-search-tags) already permit topic tags, and some ingests carry them today. A source tag currently supports source-scoped search; it does not put the ingest in the published member list. Address both new ingests and the existing corpus. Do not tag immutable snapshots or treat a relevant source as an adopted KB claim.
- For each proposed expansion, distinguish permission to tag an artifact from inclusion in tag membership. Before changing either, identify the lookup it would improve, the artifact types affected, and any standing exclusion it would reverse. Universal participation is an open question, not a rollout decision. Bring proposed reversals of explicit operator decisions back to the operator before migration.
- Review instructions that **consume** tags as well as those that assign them. For example, finding source evidence and finding Commonplace theory on the same topic need different collection scopes; auditing a head needs the whole declared membership instead. Check representative searches against known matches and against same-tag artifacts that should not be returned. Carry the resulting distinctions through affected instructions, validation and published navigation where applicable.

## Prerequisite: separate workflow state from retained reports

Workflow state already has its own Git repository. Workflows produce many changes that matter when inspecting a run but would make substantive KB changes harder to find in the main Git history.

On 2026-11-23 the operator chose to align the collection boundary with that existing Git boundary before reorganizing tags. A reader looking for a citable report should be able to search the reports collection without knowing which subtree to exclude. Someone investigating why a run stopped should be able to search the workflow state collection directly. Existing exclusions work; the split makes the choice of search scope explicit. Retained reports remain citable from a clean checkout. Each workflow decides when its state can be removed.

[ADR 128](../../reference/adr/128-one-ignored-operational-tree-under-kb-reports-state.md) now places the state checkout at `kb/workflow-state/data/`. The main repository ignores this whole directory. Current workflows use `data/current/<workflow>/`. Completed pre-move runs remain beside `current/` with their original file contents and Git history (checkpoint `c30b3818`). Their embedded paths are evidence, not a promise that current instructions can resume them; no old-path alias is needed. A historical comparison will need its own instructions. The [cutover checks](./state-cutover.md) record how the move was verified. For tag maintenance, exclude workflow state as a collection. Keep the separate exclusions for exact captures under `reports/retained/`.

## Decision: retire the completeness mark

The operator chose to retire `complete` from tag heads. In the operator’s experience, agents check membership even when a head says they can stop. Maintaining the mark therefore costs editorial work without saving the lookup it was meant to replace. The new rule is: **a tag head is selective. It introduces the topic and recommends where to start.** Use the generated listing or an exact membership query when the task calls for every member. A small head may happen to link every member. Do not require an omission or replace `complete: true` with `complete: false`.

[ADR 140](../../reference/adr/140-tag-heads-are-selective.md) implements this decision. All 21 marked heads keep their editorial links. The schema rejects the retired field; validating a note no longer checks one-hop coverage or expands the validation target to its head. Membership, head existence and size checks remain independent. Grouping generated listings by collection and changing `participating:` remain separate decisions.

## Closure

Close when the corrected maintenance instruction has been used, the audit findings have been repaired or explicitly deferred, and source tagging works for ongoing ingestion with a recorded disposition for the backlog. Record which other collections join, remain search-only or stay outside tagging, and why. Verify that affected searches return the intended kinds of artifacts and that generated listings agree with exact membership queries and no instruction treats a curated head as exhaustive. Keep findings, newly discovered dependencies and unresolved decisions here while work is active; extract lasting rules into their owning contracts and instructions before removing the workshop and its active-list entry.
