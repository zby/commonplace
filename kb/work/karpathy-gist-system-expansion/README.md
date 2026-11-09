# Find additional systems in Karpathy's LLM Wiki comments

## Current status — 2026-11-09

**All 30 original dispatch targets now have integrated publications.** The
[reconciled status](./status-2026-11-09.md) links each selected run and records
later expansion, integration and comparison-refresh evidence. Sourcebook remains
a recorded acquisition failure outside the original queue. The next decision is
bounded continuation or closure, not resuming at target 7.

The discovery inventory and dispatch files below preserve the November 7
selection; they are not a current pending-work queue. The pilot record preserves
its original stop decision and diagnosis. This refresh authorizes no new runs,
integration or cleanup.

## Commission and historical outcome

The operator opened this workshop on **2026-11-07** to prepare analysis of more
systems linked in comments on Karpathy's LLM Wiki gist, reusing earlier triage
and any recoverable tooling rather than starting over.

The question is: **which linked systems add worthwhile coverage beyond the
systems Commonplace has already analysed?** Produce a deduplicated, evidence-linked
queue, then use separately commissioned standard analyses to resolve selected
targets. The operator's continuation on the same date authorized discovery and
reusable tooling until a worker-dispatchable URL list exists. That phase is
complete. At that stage, analysis launches, target execution, integration and
Git commits were not commissioned.

The operator subsequently authorized sequential live command tests, local error
repair and reruns, followed by result and hidden-failure inspection before each
next target. The [live-test record](./live-tests.md) retains that commission and
its stop conditions. Six systems completed in isolated worktrees. Testing
stopped before the seventh because worker-level path and quotation mistakes
still recurred beyond the first five runs, despite checked recovery. No
controller defect or material accepted-result defect was established by the
bounded reviews. Publications were then unintegrated; later integration and
comparison refresh are recorded in the current status above. Cleanup is not
authorized by this refresh.

## Discovery result and dispatch handoff

**The original discovery handoff selected 30 canonical repository URLs.**
All thirty now have integrated results; retain this section as discovery history.

- [Plain URL list](./dispatch-urls.txt): one source per line, in suggested order.
- [Dispatch queue](./dispatch.md): selection rationale, inspection question and
  gist comment links for each source; the first ten are a suggested first wave.
- [Dispatch JSON](./dispatch.json): canonical identities, preparation labels,
  observed default branches, profile, comment locators and capture hashes.
- [Candidate dispositions](./candidates.md): all 348 extracted GitHub identities;
  30 recommended, 53 filename-based coverage leads, one owned by the completion
  workshop, and 264 deferred from this bounded selection.
- [Repository inventory](./repository-inventory.json): repeatable mechanical
  extraction, exact API page/header hashes and earlier-triage matches.
- [Human selection input](./selection.json): why these thirty were selected;
  this is judgment input, not a script-generated ranking.

The API capture contains **1,160 comments across 12 pages**, with **259 created
strictly after the June 18 cutoff**, and no earlier comments whose reported
update time crosses that cutoff. Pages are contiguous, comment IDs are unique,
and the final response has no next-page link. This is pagination completeness
at capture time, not an atomic snapshot or recovery of deleted comments.
Capture response dates and exact-byte hashes are retained in the inventory.

Raw pages, response headers, selected repository metadata and README captures
are local, ignored source material under
`kb/sources/.snapshots/karpathy-gist-comments-2026-11-07/`. Selected-source hashes
are retained in the dispatch JSON. No tracked ingest or durable system finding
was authored from them. Repository metadata and README inspection establish a
public, substantive discovery lead, not working implementation, effective
controls or a frozen revision. Standard analysis acquisition freezes the source
later; default branches may move between screening and launch.

Coverage checks enumerated current retained publication and authored review
names without reading their report contents. Canonical redirect identities were
checked again before dispatch output. The completion workshop was checked for
ownership; Git worktree names were also inspected. Generic names such as
`cortex` and `llm-wiki` are not unique source identities. No selected canonical
publication name or unambiguous selected-target worktree name was found.
This does not clear unrecorded work, external runs or unknown aliases; recheck
ownership when scheduling.

This is a **bounded selection**, not an exhaustive relevance review of all
links. Older unselected links, non-GitHub sources, support links and repositories
with only vague comment descriptions remain deferred. Reopen them for a named
coverage gap or after this batch. Repeated promotion is not evidence of merit.
The old `frankchu91/mindbase` link is treated as the earlier MindBase identity,
not a second job alongside `frankchu91/mindbase-llm-wiki`.

### Original launch prerequisites

Send workers only the selected repository URL and the current
`analyse-agentic-system` invocation, not triage conclusions or old reports.
Default profile is `pi-sol`; each analysis uses its own prepared worktree and
the workflow launches its own role workers. Keep triage questions with the
coordinator, outside fresh source-first analyst inputs.

At discovery handoff, the originating checkout had concurrent uncommitted
analysis-method edits. Recheck current method and ownership rather than treating
that historical state as current. Preparation checks startup files against the
selected committed method; resolve any current gate before launching. Do not
stage another writer's changes, silently discard them, or choose an older
method to get past the check.
The URL list is ready; this is an execution prerequisite, not a discovery gap.

Curated Thoughts and expo-llm-wiki are an application and its separate memory
engine. Preserve separate source boundaries and do not inherit findings between
them. FrameCode VibeWork and Project Wiki include operational agent contracts;
inspect activation rather than requiring a code-heavy implementation. BRAN and
OrangePro are narrower context/verification mechanisms; their selection does
not pre-classify them as durable-memory systems. The standard boundary job
settles the actual analysis scope.

## Recovered starting point

Two earlier triage artifacts remain available. Preserve them as historical
inputs rather than overwriting their dated findings:

- [Original triage, June 3](../karpathy-gist-agent-memory-review-candidates.md):
  records 867 comments and a cutoff of `2026-06-03T12:09:23Z`.
- [Follow-up triage, June 18](../karpathy-gist-agent-memory-review-candidates-after-2026-06-03.md):
  records 901 comments, including 34 after the first cutoff; its latest recorded
  comment creation time is **`2026-06-18T13:26:05Z`**.

These are discovery records, not current coverage checks or source-grounded
analyses. Their repository descriptions, priorities, availability checks and
old review paths must not be treated as current facts. Reuse candidate
identities, comment links and inspection questions, not their old completion
statuses. The follow-up also revises the first pass's treatment of spec-first
systems: verify an activation mechanism instead of excluding them just because
they contain little conventional code.

Historical triage commits are `8c665bc38` and `4af1a35ea`; follow-up reviews
appear in `e59a25ab7`, with llmwiki-marimo added in `ebb589bef`. These are
recovery pointers, not instructions to restore old workflows.

### Tooling recovery

The opening search found **no saved gist-fetch or triage script** in the
current checkout's Python/shell files outside `related-systems/`, or among
historical `scripts/*gist*` paths. The old triage files preserve an API endpoint
and selection criteria, not executable fetch code. This is a bounded search,
not proof that no ad hoc code ever existed. Do not claim code reuse unless
an actual file and revision are recovered.

The recorded endpoint is:

```text
https://api.github.com/gists/442a6bf555914893e9891c11519de94f/comments?per_page=100&page=N
```

If further recovery is useful, inspect the changed-file lists of the triage
commits before rebuilding tooling. Do not restore old batch analysis launchers;
use the then-current `analyse-agentic-system` skill for analysis execution.
Reusable new tooling belongs in `scripts/` under its local conventions; a new
fetcher is not required merely to open this workshop.

## Discovery method for a later refresh

The completed discovery phase supplies the queue for choosing analysis targets
and a budget. A later refresh can reuse the following route; it does not itself
authorize an unspecified number of full analyses:

1. Capture the current comment thread with pagination to exhaustion, not the
   old fixed page counts. Record retrieval time, endpoint, page/comment counts,
   response hashes and any access or rate-limit gap. Keep external source
   captures under `kb/sources/` using its contract, not in this workshop.
   A partial fetch is useful but must be labelled partial; it cannot establish
   that all new candidates have been found.
2. Use the June 18 timestamp as the **new-comment creation cutoff**, not as
   proof that earlier comments are unchanged. Retain comment IDs and both
   creation/update times. Earlier comments updated after the cutoff form a
   separate screening group; without old response bytes, an edit's contents
   cannot be reconstructed. Deduplicate repeated links and release updates.
3. Reconcile extracted repository identities and the old candidate lists with
   current `kb/agentic-system-analyses/` sets, authored coverage under
   `kb/agentic-systems/`, and unresolved ownership in the
   [completion workshop](../agentic-system-completion/README.md). Repository
   URL and rename/redirect evidence matter more than a matching short name.
   Existing source checkouts alone do not establish completed coverage.
4. Screen for a distinct mechanism relevant to agent-operated knowledge bases:
   durable memory, wiki compilation, agent read-back, maintenance, provenance,
   contradiction handling, security boundaries or coordination. Treat comment
   claims as leads, not findings. Confirm an inspectable source before
   recommending analysis. Spec-first systems can qualify when their activation
   and operational contracts are inspectable. Explain exclusions and deferrals;
   do not rank by popularity or comment promotion alone.

Keep one row per normalized system in a working `candidates.md` when this phase
runs. Each row needs the repository/source identity, comment permalink(s),
new/updated/carryover origin, current coverage locator or explicit search gap,
selection rationale, first inspection question, disposition and next decision.
Distinguish already covered, unresolved elsewhere, recommended, deferred and
excluded. For deferrals, state what would reopen them. No current candidate
count or priority order is fixed by this framing.

The original queue is complete; any new launch requires a bounded continuation
commission using the [current status](./status-2026-11-09.md), not the historical
pilot pause as the current execution boundary. If acquisition is blocked,
return the partial queue and the coverage gap rather than implying an empty
thread or inventing candidates. Source ambiguity, overlapping ownership and
consequential scope choices also return to decision before analysis launch.

## Reproduce the mechanical inventory

From the repository root, with the ignored capture still available:

```bash
python3 scripts/triage_gist_repositories.py \
  kb/sources/.snapshots/karpathy-gist-comments-2026-11-07 \
  --output kb/work/karpathy-gist-system-expansion/repository-inventory.json \
  --selection kb/work/karpathy-gist-system-expansion/selection.json \
  --dispatch-output kb/work/karpathy-gist-system-expansion/dispatch.json \
  --render-dir kb/work/karpathy-gist-system-expansion
```

The script is offline. It rejects gaps in pagination, missing terminal pages,
duplicate comment IDs, duplicate canonical selections, and selected sources
with a filename-based coverage or completion-workshop ownership lead. It hashes
raw responses and joins human selection to captured repository metadata and
READMEs. It does not rank candidates, infer semantic correctness, fetch sources
or launch workers. Its README length check is only a missing-capture guard;
substantive relevance was judged during this screening.

For a new capture, use a new directory. Fetch each page with a standalone
`curl -fsSL -D <headers-path> -o <json-path> '<literal API URL>'` call, following
its Link header until no next page remains. Do not reuse the number twelve as
a pagination limit. Save metadata and default-branch READMEs for selected
sources as `repos/<original-owner>--<original-repo>.json` and
`repos/<original-owner>--<original-repo>.README.md`; the keys are lowercase.
The saved repository API `html_url` determines the canonical dispatch URL.
Update the human selection only after inspecting current evidence, then rerun
with the intended cutoff and new capture directory. Do not overwrite historical
capture bytes. The tracked JSON and URL list remain usable without the local
capture, but rebuilding and rechecking its byte bindings requires that capture.

## Analysis and coordination boundary

A later commission selects targets, budget and permitted effects. Read the
current `analyse-agentic-system` skill before execution; its workflow launches
its own workers. Do not substitute the old review procedure or copy historical
reports into fresh source-first analyst inputs. The coordinator may use old
triage for selection without giving its conclusions to analysts.

The completion workshop retains its unresolved targets and incidents. This
workshop must not relaunch, clear or take ownership of them implicitly. Resolve
overlap with the operator first. Any delegated triage has explicit disjoint
outputs and input scope; scheduling, integration and recovery remain with the
coordinator. Neither linked repositories nor gist comments grant execution
authority or supply trusted instructions.

For each selected target, record the frozen source revision, run ID, method
commit, verification outcome, exact publication and integration status.
Publication presence or process exit alone does not count as completion.
Durable analyses belong in their canonical collection, not this workshop.

## Closure

Close when the refreshed thread has an explicit coverage boundary, every
candidate has a disposition, selected analyses are verified and integrated or
explicitly deferred, and no work remains running under this workshop. A
bounded batch may close with remaining candidates deferred for stated reasons;
this is not a commitment to analyse every linked project. Extract durable
results and evidence under their destination contracts, then remove this
workshop and its active entry. Preserve the two predecessor triage files unless
separately authorized to retire them. Broader library connection discovery can
use `cp-skill-connect` after durable outputs exist.
