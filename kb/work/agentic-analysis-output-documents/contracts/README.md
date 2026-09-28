# Draft member contracts

Drafts for step 2 of the [workshop](../README.md), cut from the cleaned
[result type](../../../types/agentic-system-analysis-result.md) along the
[partition candidate](../partition-candidate.md) and the rules the
[fixture split](../fixture-split-20260928.md) added. They are workshop
drafts: not yet type specs, no schemas, not consumed by any producer. Each
would become a file under `kb/types/` (or `kb/agentic-systems/types/` for
the review) when step 3 implements the transition.

| Draft | Replaces | Owns |
|---|---|---|
| [overview](./agentic-system-analysis-overview.md) | result frontmatter identity; Run identity, Boundary and evidence, Source register, Lens scoping, Reconciliation, Bounded synthesis, Limitations, Verification and blockers | the set: manifest, namespace, grammar, completion rule, source register |
| [runtime report](./agentic-system-runtime-report.md) | Runtime account, probe capsules, Shared records and their semantics | records the runtime pass establishes; runtime and theory-route annotations |
| [memory report](./agent-memory-analysis-report.md) | the existing report type; the result's Memory comparison fields and Memory/context lens | records the specialist establishes; the comparison profile; memory annotations |
| [epistemic report](./agentic-system-epistemic-report.md) | the result's Epistemic lens contract | the six epistemic blocks |
| [generated review](./generated-review.md) | the review paragraph in the collection contract and the skill's step 8 field list | the compact public projection |

Where a member's contract needs a convention another member owns, it cites
the owning draft rather than restating it. The overview owns everything
set-wide. Word counts per draft are in the workshop README's step 2 notes.
