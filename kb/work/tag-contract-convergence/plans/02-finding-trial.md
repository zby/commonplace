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

## Acceptance

- Every condition covered the same member set, and each grouped page was
  checked against the resolver.
- Results name the tasks, finders, and misses, not only preferences.
- The workshop README and plans reflect the decision before Phase 3 starts.
