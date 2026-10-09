# The analysis set's layout

The `agentic-system-analysis-set` type's layout as it stands after
[ADR 114](../../reference/adr/114-directory-types-declare-what-a-role-verifies.md),
written out role by role so that the relations the engine derives can be
read without parsing the frontmatter. The `verifies` column is the ADR's
addition and is not yet in the type spec.

## Roles

Every role is one file at the artifact root. Every role except the boundary
copies `run-id` and `reviewed-boundary` from the boundary; the overview
copies five more fields and the profile also copies `source-identity` from
the memory report. Names are the roles' names; `b, r, m, e` stand for
boundary, runtime, memory, epistemic.

| Role | File | Cites | Verifies | Verified by | Required |
|---|---|---|---|---|---|
| boundary | `boundary.md` | itself | | | always |
| overview | `overview.md` | b r m e | | | always |
| runtime | `runtime.md` | b r m e | | record-verification | complete |
| memory | `memory.md` | b r m e | | record-verification | complete |
| epistemic | `epistemic.md` | b r m e | | record-verification | complete |
| reconciliation | `reconciliation.md` | b r m e | | record-verification | complete |
| memory-profile | `memory-profile.md` | r m e | | profile-verification | complete |
| synthesis | `synthesis.md` | b r m e | | synthesis-verification | complete |
| record-verification | `record-verification.md` | b r m e reconciliation | r m e reconciliation | | complete |
| profile-verification | `profile-verification.md` | r m e memory-profile | memory-profile | | complete |
| synthesis-verification | `synthesis-verification.md` | b r m e synthesis | synthesis | | complete |

"Required: complete" means the role is present when the boundary's
`result-disposition` is `complete`; a `blocked` or `out-of-scope` instance
has only the boundary and the overview, and may have nothing else.

## What each relation means and who covers it

The engine derives one relation per entry in the three relation columns,
named `<role>:<kind>:<partner>`. Publication needs every one between
present members covered by an accepted judgment of the current versions.

| Kind | Meaning | Checked by | Covered by |
|---|---|---|---|
| `identity` | this role repeats fields from the partner | the validator, in the role's content check | the role's check job accepting the candidate |
| `cites` | this role's references resolve against the partner's declarations | the validator, in the role's content check | the role's check job accepting the candidate |
| `verifies` | this role has judged the partner | nothing structural | the apply job judging the partner's handed version |

So `memory:cites:runtime` is covered when `check-memory` accepts a memory
candidate whose references into the runtime report resolve, and
`record-verification:verifies:memory` is covered when `apply-verify`
reads a blocker-free verdict and accepts the memory version the verifier
was handed. A verdict's own content check covers its `cites` to the
reports, never its `verifies`.

## The verifiers' subjects

| Verifier | Cites | Verifies | Difference |
|---|---|---|---|
| record-verification | boundary, the four records | the four records | cites the boundary, does not verify it |
| profile-verification | the three reports, memory-profile | memory-profile | cites the reports as evidence, verifies only the profile |
| synthesis-verification | boundary, the three reports, synthesis | synthesis | same shape as the profile's |

Each verifier cites what it verifies because its blockers reference record
IDs in those members. It cites more than it verifies because its evidence
reaches further than its judgment.

## What a plan reads from this

- One check job per role, scoped to that role's `identity` and `cites`
  relations to the partners in its snapshot.
- One apply job per role with a `verifies` list, judging the handed
  versions of the listed roles over the `verifies` relations.
- Judgment gates named by `verifies` relations: the profile waits on
  `record-verification:verifies:memory` and its three siblings; the
  synthesis waits on those and `profile-verification:verifies:memory-profile`.
- Publication when every role the disposition requires is present and
  every relation above is covered.
