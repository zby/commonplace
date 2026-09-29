---
description: "Proposal: cut the scoping job, the memory handoff protocol and the review job from agentic-system analysis, derive the public review from the verified overview, and fix source identity and the blockers form in code"
type: reference/types/design-proposal.md
---

# Fewer authored decisions in agentic-system analysis

An agentic-system analysis still asks workers to make decisions whose alternatives change nothing in the result, and then asks later steps to reconcile them. The operator selected five cuts on 2026-09-29 from the workshop's simplification candidates (`kb/work/analysis-offload-to-code/simplification-candidates.md`, Decisions 1, 2, 3, 5 and 6). This proposal states the contract changes they need and the small design choices the decisions left open.

## Current state (as of 2026-09-29)

After [ADR 096](../adr/096-analysis-passes-declare-their-own-records-under-lens-prefixes.md):

- A `scoping` job runs between the runtime pass and the lenses. It chooses `brief` or `full` depth for each lens and names trigger records; no code reads the depth. The overview renders its output as `## Lens scoping`. Both lens members state their scope again: the memory profile's `scope`, and block 1 of the epistemic report.
- Code writes `memory-input.md` (boundary, source, the scoping record's memory part, and the runtime member). The memory method (`analyse-agent-memory.md`) describes a private handoff: the specialist hashes its input and method by hand, and the member carries `canonical-register-sha256`, `method-sha256` and `worker-model`. `_verify_memory_member` checks only the first, against `memory-input.md`, which is gitignored run state, so no clean checkout can verify it. Nothing checks the other two beyond presence; `inputs-commit` already pins the method.
- A `review` job writes `review-body.md` after verification: a description, an `Evidence basis:` line and prose. `review_body_refusals` checks only the H1, that line and the description. No check covers the prose, which restates the Bounded synthesis.
- The caller gives `source-identity` at opening, and the boundary worker writes `source.identity` independently. Nothing compares the two. `_check_incumbent` compares identities by exact string, so a difference of form (a trailing `.git` or `/`) fails at publication, after the whole analysis ran.
- The workflow continues only when the verification's Blockers text, lowercased and without a final period, equals `none`. "None found" counts as a blocker, and in the last round it stops the run.

## Proposed changes

**1. No scoping job, no depth, no memory handoff.** Delete the `scoping` job, `memory-input.md` and its generator, and the overview's `## Lens scoping` section. The memory and epistemic jobs read `boundary.md` and `output/runtime.md` directly, under the same input and completion contract as every other job. Each lens states its scope in its own member, as it already does. Remove the private handoff protocol from `analyse-agent-memory.md`: manual hashing, notifications, and the returned path, hash and status.

**2. Fewer memory frontmatter fields.** Drop `canonical-register-sha256`, `method-sha256` and `worker-model` from the memory report type. With them goes `_verify_memory_member`. Model identity stays in the workflow's operational state.

**3. The public review is a projection.** Delete the `review` job and `review-body.md`. Code renders the review body from the verified overview:

- `# <System>`;
- an `Evidence basis:` line built from the boundary fields (`evidence-tier`, `analysis-cutoff`, source identity, `reviewed-boundary`);
- the Bounded synthesis;
- `## Limitations` with the Limitations text.

Relative links in that text point inside the set directory, so code rewrites them to resolve from the review's location, into the retained set. The reconciliation writes a `## Description` section holding one sentence. Code uses it as the overview's `description` and as the review's `description`. It is thus part of what verification reads. A blocked or out-of-scope overview keeps its code-written description. The generated review type's Body section changes to describe the projection.

**4. One normalized source identity.** Code normalizes the `source-identity` parameter once, before anything uses it. It strips surrounding whitespace, a trailing `/` and a trailing `.git`, and lowercases a URL's scheme and host. The run slug, the incumbent inspection and publication then use that one identity. The boundary job's prompt gives it, and the boundary validator refuses a `source.identity` that differs from it. Removing `review-path` stays deferred.

**5. One form for Blockers.** The verify job's validator accepts a `### Blockers` section only when it is exactly `none` or a Markdown list whose entries start with `- `. The workflow continues on exactly `none`. No structured fields are added.

## Forces

- Each cut removes a decision a worker made and a later step had to accept, restate or check. None of them removes a check that ran: no code read the depth, the two unchecked hashes or the model field, and the review prose was unchecked.
- Public reviews get longer. On the PageIndex set, the review body had 464 words, the Bounded synthesis 611 and the Limitations 220. The operator accepted the length.
- The Bounded synthesis now has two readers: the overview's reader and the public reader. The overview type's Bounded synthesis contract has to say so, because a synthesis written only for the set's reader can lean on member context.
- Normalization is limited to forms of one URL. It does not decide whether two different URLs name one repository.

## Free choices

- Where the description lives. This proposal puts it in the overview as the reconciliation's `## Description`, so verification reads it. It could instead stay outside the set, in a side file the reconciliation writes; then nothing checks it.
- The exact normalization rules beyond the stated ones, such as dropping `www.`.

## Operativity

Code consumes the changes in `agentic_workflow.py`, `agentic_analysis.py`, `agentic_publication.py` and `agentic_set.py`. The overview, memory report and generated review type specs and their schemas change. So do the job instructions under `kb/instructions/analyse-agentic-system/jobs/` and the two method instructions, which workers load with binding force. The change takes effect for runs opened after the commit that lands it.

## Adoption criteria

The operator selected these changes on 2026-09-29, and they land before the second real run. That run is the joint test: it should publish with no scoping, handoff or review-writing job. The run cannot isolate the effect of any single change.
