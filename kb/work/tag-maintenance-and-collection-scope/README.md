# Tag maintenance and collection scope

Posed by the operator on 2026-11-23. Make tag maintenance usable again, run it against the existing KB, and make tracked sources routinely findable by topic. Decide whether other collections should use tags. A long interval since the last audit is a reason to inspect the structure, not evidence that a particular tag needs changing.

The [search-command ledger](./search-command-ledger.md) records which instructions search by topic, which require exact membership, and which must keep a wider scope to find dependencies.

## Where the work starts

- The [search checks](./search-checks.md) verified the corrected [maintenance instruction](../../instructions/maintain-curated-indexes.md) against the [tag contract](../../tags/COLLECTION.md). Use it next to assess heads, assignments and eligible but untagged material. A passing validator cannot tell whether a head helps a writer distinguish two neighboring topics.
- [Tracked source analyses](../../sources/COLLECTION.md#topic-search-tags) already permit topic tags, and some ingests carry them today. At the start of this workshop a source tag supported source-scoped search but did not put the ingest in the published member list. Address both new ingests and the existing corpus. Do not tag immutable snapshots or treat a relevant source as an adopted KB claim.
- For each proposed expansion, distinguish permission to tag an artifact from inclusion in tag membership. Before changing either, identify the lookup it would improve, the artifact types affected, and any standing exclusion it would reverse. The decision below changes enumeration, not authoring permission. Bring proposed reversals of explicit operator decisions back to the operator before migration.
- Review instructions that **consume** tags as well as those that assign them. For example, finding source evidence and finding Commonplace theory on the same topic need different collection scopes; auditing a head needs its exact member list instead. Check representative searches against known matches and against same-tag artifacts that should not be returned. Carry the resulting distinctions through affected instructions, validation and published navigation where applicable.

## Prerequisite: separate workflow state from retained reports

Workflow state already has its own Git repository. Workflows produce many changes that matter when inspecting a run but would make substantive KB changes harder to find in the main Git history.

On 2026-11-23 the operator chose to align the collection boundary with that existing Git boundary before reorganizing tags. A reader looking for a citable report should be able to search the reports collection without knowing which subtree to exclude. Someone investigating why a run stopped should be able to search the workflow state collection directly. Existing exclusions work; the split makes the choice of search scope explicit. Retained reports remain citable from a clean checkout. Each workflow decides when its state can be removed.

[ADR 128](../../reference/adr/128-one-ignored-operational-tree-under-kb-reports-state.md) now places the state checkout at `kb/workflow-state/data/`. The main repository ignores this whole directory. Current workflows use `data/current/<workflow>/`. Completed pre-move runs remain beside `current/` with their original file contents and Git history (checkpoint `c30b3818`). Their embedded paths are evidence, not a promise that current instructions can resume them; no old-path alias is needed. A historical comparison will need its own instructions. The [cutover checks](./state-cutover.md) record how the move was verified. For tag maintenance, exclude workflow state as a collection. Keep the separate exclusions for exact captures under `reports/retained/`.

## Decision: retire the completeness mark

The operator chose to retire `complete` from tag heads. In the operator’s experience, agents check membership even when a head says they can stop. Maintaining the mark therefore costs editorial work without saving the lookup it was meant to replace. The new rule is: **a tag head is selective. It introduces the topic and recommends where to start.** Use the generated listing or an exact membership query when the task calls for every member. A small head may happen to link every member. Do not require an omission or replace `complete: true` with `complete: false`.

[ADR 140](../../reference/adr/140-tag-heads-are-selective.md) implements this decision. All 21 marked heads keep their editorial links. The schema rejects the retired field; validating a note no longer checks one-hop coverage or expands the validation target to its head. Membership, head existence and size checks remain independent. ADR 140 left grouping and `participating:` for the next decision.

## Decision: list members by collection

[ADR 141](../../reference/adr/141-list-tag-members-by-collection.md) replaces `participating:` with generated groups. The exact listing includes editorial picks and tagged source analyses, but skips workflow state and source snapshots before traversal. The checkout's `continual-learning` group gained two existing source ingests alongside 28 theory artifacts without retagging. The operator removed the headless `foundations` tag from the Ashby source review; its `computational-model` tag remains.

## Decision: one route for continual learning

Retire the separate `deploy-time-learning` tag. Its distinction from `continual-learning` did not help navigation. Keep timing in the claim when it matters, not as a sub-tag or a dedicated navigation section. The mainstream term needs no new KB definition.

Review mentions separately from tag assignments. From the checkout root, `git grep -inEi 'deploy(ment)?[- ]time[- ]learning'` finds old labels, domains, discussion and historical paths without walking snapshots or local run data. Also check split-line and typographic variants. A hit is not automatically an edit:

- In authored explanations, say what changes and when. For instance, a contrast between a trained policy and a retained instruction is a contrast between mechanisms, not a contrast with continual learning. Preserve the narrower claim.
- For link labels inherited from an old note title, name the actual destination. Review source analysis and source-specific search terms separately from verbatim quotations, which must not be rewritten.
- Keep historical filenames, redirect keys, retained evidence, and published versions intact. Inspect current workshop instructions separately from captured plans and logs.

The first prose pass revised the 18 theory notes using the retired phrase. The context-engineering note now distinguishes using a decision in one session from revising how later sessions retrieve it. The source pass began with the AgeMem, Amodei, and “Why AI systems don't learn” ingests, separating where a change is retained from who selects it. A case-insensitive search allowing whitespace and dash variants found no further uses of the phrase in `kb/theory/` and 51 remaining tracked source files with matches. Review those in context; a quoted source term is not a cleanup target. Other collections and current workshop prose remain to check.

## Assignment audit: continual learning in source ingests

Reviewed 22 tracked ingests: those already tagged `continual-learning` and those whose `domains` contained `continual-learning`, `continuous-learning`, or `lifelong-learning`. Domains selected candidates; the ingest's analysis decided membership. Kept the two existing members and added 18. For example, the Amodei ingest examines the argument that lasting updates may be unnecessary; the LibContinual ingest explains how changing access to earlier tasks changes method rankings. Both belong on the reading list. Left two candidates untagged for this topic: the Mobius ingest evaluates an architecture rather than a continuing update process, and the knowledge-detection ingest evaluates a filtered training set rather than learning over a succession of tasks. Their search terms remain useful.

Corrected the `improvement-loop` head's obsolete restriction of continual learning to non-weight updates. Restored the declared `learning-theory` parent on child members that lacked it. The exact query now returns 20 source ingests and 31 theory notes; all 51 also carry the parent. This was not a search of every ingest body. A next pass can look for descriptions of retention, transfer or forgetting across tasks in ingests that lack these domain terms. This assignment audit did not change the terminology-review backlog.

### Search beyond the domain terms

Excluding the first pass's candidates, searched tracked ingest descriptions and summaries for learning or adaptation across experiences, transfer to later tasks, loss of earlier tasks, and explicit mentions of continual or lifelong learning. Reviewed 15 matches and spot-checked three additional reports on workflow reuse or forgetting. Added 10 ingests; left eight without this tag. This is a bounded search, not an assertion that the rest of the corpus is irrelevant.

- Agent Workflow Memory analyzes how an earlier successful trajectory becomes a workflow used on a later web task. Reflexion analyzes a narrower case: feedback changes the next attempt on the *same* task, but the evaluations do not establish cross-task transfer. Both answer a reader's question about what carries forward.
- The web-agent long-context benchmark puts irrelevant prior tasks into context to measure distraction; it does not study learning from them. The Geometry of Forgetting explains retrieval interference rather than loss of a learned capability after an update. The terms suggested both candidates, not membership.
- Other near misses left unchanged: Corral and Socratic Agents analyze scientific reasoning within an episode; the two Pathway reports address a benchmark and a formal architecture; the adaptive-forgetting report evaluates a retrieval budget; the multi-agent infrastructure essay uses possible future learning to motivate a prediction about orchestration.

The exact list now has 30 source ingests and 31 theory notes. Next audit `improvement-loop`: compare candidate admission and rejection with recurring execution that proposes no change. Start with ingests about harness optimization already reviewed for continual learning, without assuming that either tag implies the other.

## Assignment audit: improvement loops in source ingests

Reviewed all 11 existing source assignments and kept them. A separate acceptance test is not required for membership: AlphaZero explains what changed when the predecessor's match gate was removed; Soar explains when a new rule is installed and how it controls later search. Argyris belongs for a different reason: defensive routines prevent evidence of failure from prompting reconsideration of the governing policy. These are distinct reading routes, not claims that all three use proposal selection.

Reviewed nine neighbors. Added AutoSaddler, Agent Optimizers Compound, and Harness Continual Learning for their patch or regression checks; JAZ and Long-Horizon Agents for how a correction enters later prompts, tools, or guards; Hyra for the evidence required to promote research lessons; and the text-optimization essay for its comparison of competing text revisions before adoption. In the Long-Horizon Agents case it is the move from repeated instructions to an executable worker-stop guard that matters, not the number of ticks. Hyra describes a promotion procedure but does not show a promoted entry improving a later decision.

Left LibContinual and Effective Harnesses for Long-Running Agents without this tag. LibContinual compares learning methods under different evaluation protocols; the benchmark does not decide which update a learner keeps. The long-running coding harness checks whether an application feature is complete so the next session can continue; that is not a decision to change how later sessions work.

The exact lookup now has 18 source ingests. All carry the declared parent `self-improving-systems` and its parent `learning-theory`. The next comparison is outside sources: check whether the existing theory assignments respect the same distinction between changing a work product and changing the procedure that produces it.

## Closure

Close when the corrected maintenance instruction has been used, the audit findings have been repaired or explicitly deferred, and source tagging works for ongoing ingestion with a recorded disposition for the backlog. Record any proposed changes to which artifacts authors should tag and why. Verify that affected searches return the intended kinds of artifacts and that generated listings agree with exact membership queries and no instruction treats a curated head as exhaustive. Keep findings, newly discovered dependencies and unresolved decisions here while work is active; extract lasting rules into their owning contracts and instructions before removing the workshop and its active-list entry.
