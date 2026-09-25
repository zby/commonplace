# Phase 2 — Test whether any tag page helps find things

**State:** waits for Phase 1's resolver. Its outcome decides the scope of
Phases 3 and 4.

## Why this runs before the contract work

On 2026-09-25 the operator reported that they had stopped using tags because
tag pages do not help them find things. The earlier plan made membership exact
first and tested usefulness last. That order spends the contract, head, and
migration work on a feature nobody relies on. This trial asks first whether
any tag page helps finding. Phases 3 and 4 then build only what the result
supports.

The candidate designs come from the [tag maintenance and derived browsing
proposal](../../../reference/proposals/tag-maintenance-and-derived-browsing.md),
which records Gwern's tag pages and the "Sort By Magic" topic grouping. This
trial takes only the finding-related options. Suggested assignments, rejected
suggestions, and aliases address maintenance cost, which the operator did not
report as the problem.

## Prior evidence: agents rarely use tags to find things

A 2026-09-25 survey of session transcripts checked whether agents already use
tags to navigate. It covered 6,342 Codex sessions in Commonplace-using
projects (March–September 2026) and 496 Claude Code sessions
(August–September 2026). Tool calls were extracted and classified with
regexes.

- Tag search is about 1% of KB search. Content `rg` is about 45 times as
  frequent, and description `rg` about 7 times.
- Most tag-page reads and tag searches come from work on the tag system itself
  or from `cp-skill-connect`, whose procedure prescribes them. Outside those,
  tag pages are read in fewer than 2% of Codex sessions and about 4% of Claude
  sessions, usually alongside content search.
- In installing projects agents almost never use tags: llm-do has about 23,000
  tool calls and no tag searches.
- The `complete` mark changed agent behavior only inside the connect procedure.
  No use of `covered_by` was found.
- The operator's own positive remark (2026-08-21) was about human readers of
  the published site finding all systems under one tag.

Limits: the regex classes are coarse, Claude transcripts start in August, and
reasoning is invisible, so a tag page that informed a choice without a
follow-up call would be missed. The evidence is consistent with the
operator's report. Condition D below is already the agents' main finding path,
so it is the baseline any tag page has to beat. Human site use and agent use
must be judged separately.

## Conditions

Each condition covers the same tag and the same exact member set:

- **A. Current page** — the curated head as it stands, plus its generated tail
  on the published site.
- **B. Exact listing** — every member's title and one-line description, in
  resolver order. This is the page's raw material with no curation.
- **C. Grouped page** — the same members in labelled topic groups, each member
  with its description, and a short introduction. This is Gwern-style
  grouping. An agent produces the groups once from titles and descriptions,
  with no embeddings. The page is a temporary trial file in this workshop, not
  a committed head. Structural check: its member set equals the resolver set.
- **D. No tag** — the finder uses description search (`rg "^description:"`)
  and content search only. This checks whether tags add anything at all.

## Tags

Use one broad tag and one mid-sized tag, chosen by the operator. Candidates by
member count on 2026-09-25: `learning-theory` (142), `foundations` (118),
`context-engineering` (69), `kb-maintenance` (54).

## Tasks

The operator supplies 5–8 real finding tasks from recent work, such as "which
note argues X" or "what do we have on Y". At least two tasks must have relevant
items outside the tag, so that a tag page that looks complete can be caught
stopping the finder too early.

## Finders and measures

- **Operator.** For each task, use the condition's page on the surface they
  actually use (site or files). Record whether they found the target, what they
  missed, how many items they opened, and a short usefulness judgment.
- **Fresh agents.** Give each agent one task and one condition. Record the
  target found, relevant items missed (including outside the tag), files
  opened, context loaded, and whether the agent stopped early.

Keep membership fixed during the trial. Record results in this workshop.

Two constraints from the proposal carry over. A group in the grouped page
makes no completeness promise; only the whole tag can. Gwern's rule that drops
a parent tag when a child tag is present conflicts with Commonplace's split
rule and is not part of any condition.

## Decision rule

- **A grouped or exact page clearly beats A and D** for the operator or for
  agents: rewrite Phases 3–4 so the contract and canonical heads serve that
  page. The head keeps authored routing; the winning view becomes its
  generated part.
- **Nothing beats D:** tags are not a finding path. Reduce them to search
  keywords. Drop mandatory heads and the `complete`/`covered_by` marks, and
  rewrite or close Phases 3–4. That keeps only the latent-defect fix and the
  resolver.
- **Mixed result:** the operator decides, with the recorded tasks.

`cp-skill-connect` does not weigh in this decision. Its tag use may still be
useful, but it needs little: the list of a tag's members, and at most a signal
that lets it skip that search. It adapts to whichever tag system survives, so
its current reliance on heads and the `complete` mark is no reason to keep
them. Phase 3 updates connect to match.

## Acceptance

- Every condition covered the same member set, and each grouped page was
  checked against the resolver.
- Results name the tasks, finders, and misses, not only preferences.
- The workshop README and plans reflect the decision before Phase 3 starts.
