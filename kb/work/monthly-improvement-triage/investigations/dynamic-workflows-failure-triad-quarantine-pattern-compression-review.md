## Note: orchestration-needs-privilege-quarantine-not-permission-scope.md

# Compression Bundle Review: Agent orchestration needs a privilege quarantine, not just a permission scope

**Target:** `kb/notes/orchestration-needs-privilege-quarantine-not-permission-scope.md`
**Bundle:** `kb/work/agent-note-improvement/compression/`

## Overall Result

INFO

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | PASS | Title, frontmatter description, and the opening paragraph all state the same claim plainly before any supporting apparatus appears; every later section is clearly subordinate to it. |
| compression/branch-bloat | PASS | Each section (mechanism, two instances, general-principle relation, scope limit, open questions) supplies a premise, evidence, boundary condition, or credibility check the stated claim actually needs; nothing competes with the main thesis. |
| compression/detail-overhang | INFO | The GBrain bullet in "Two independent instances" is noticeably denser than its paired dynamic-workflows bullet; the consequence detail ("losing auto-linking on writes and access to protected job types") is defensible but sits right at the edge of proportionate. |
| compression/marginal-value-redundancy | PASS | "Relation to the general security-risk question" and "Scope limit" each add a distinct, non-repeated move (naming the general principle; flagging a residual risk the rest of the note doesn't cover) rather than recapping earlier text. |

## Findings

### compression/detail-overhang

- INFO: In "Two independent instances," the GBrain bullet ("every operation declares a scope (`read`/`write`/`admin`), and remote (agent-facing) callers ... are classified untrusted at the API boundary regardless of what the skill prose tells them to do, losing auto-linking on writes and access to protected job types") carries meaningfully more sub-detail than the parallel dynamic-workflows bullet in the same list. The core point needed for the convergence argument is just "GBrain denies privileged action to the agent-facing caller regardless of prose instruction" — the specific consequences (auto-linking, protected job types) make the claim concrete and are defensible, but a reviewer could compress them to a short parenthetical without losing the argument's force. Not a clear-cut violation; flagged as INFO rather than WARN because the specificity also does real work (it's the strongest evidence in the note that quarantine is enforced at the code layer, not the prose layer).

## Suggested Revision

No structural change needed. If tightening for space, shorten the GBrain bullet's trailing consequence clause ("losing auto-linking on writes and access to protected job types") to a shorter phrase (e.g., "losing write-level privileges") so the two instance bullets read as comparable in weight — but this is optional polish, not a compression failure. The note's core claim, mechanism, evidence, and scope-limiting caveat are each doing distinct, necessary work and none should be cut.
