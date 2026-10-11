# Design direction and preservation defaults

Intentions established in the operator discussion of 2026-10-11. They describe
the arrangement to aim at and the order in which to consider changes. They are
design intentions, not changes to current worker authority or contracts, and
most of them describe the [current arrangement](./current-arrangement.md)
already.

## Direction

- Keep a general architectural layer that explains the system's main
  responsibilities, components and relationships. It is not an exhaustive code
  review.
- Combine it with focused lenses. A lens is a question-driven investigation in
  a separate process, with authority to search the frozen source for relevant
  mechanisms. It is not a centrally assigned directory or a preselected code path.
- Let lenses discover mechanisms the general account missed and challenge its
  characterization. The general account must not become their evidence boundary
  for discovery. Bounding what a verifier searches for lens omissions is a
  different matter; see the
  [verification coverage bounds proposal](./proposals/verification-coverage-bounds.md).
- Reconcile the findings into a coherent overall account rather than concatenate
  specialist inventories.
- Select depth for its contribution to understanding mechanisms, design choices,
  conditions and trade-offs. Finding every implementation defect is not the goal.
- Make coverage limits explicit. Large repositories do not create an obligation
  to review every code path. Qualifications must also constrain the affected
  claims; a general disclaimer cannot excuse a misleading statement. Unknown
  coverage must not read as evidenced absence.
- Keep source characterization distinct from Commonplace adoption advice.
  Borrowing motivates the questions, but transfer assessments remain separately
  commissioned work.

## Preserve the stable process

Start by comparing these intentions with the current runtime, memory and
epistemic roles. Do not assume that new conceptual distinctions require new
jobs, report members, schemas or engine features.

Prefer the least disruptive sufficient change:

1. Clarify purpose, coverage expectations and materiality within existing roles.
2. Adjust role instructions or source-discovery boundaries where a specific
   mismatch remains.
3. Split a role or change dependencies only if the benefit justifies repeated
   discovery, additional reconciliation and migration cost.
4. Change shared machinery only for an established requirement that the existing
   machinery cannot support.

Preserve frozen evidence, source isolation, code-scheduled execution, correction
ownership, independent verification and exact-byte publication unless a specific
change is separately justified and authorized. These are preservation defaults,
not claims that every current detail is optimal.

## Vocabulary at extraction

If the comparison confirms that the runtime role is the general layer, the
workshop's phrase "general architectural layer" should not survive extraction
as a second name for it. Either the role is renamed, which is a method change
needing its own authorization, or the extracted text uses the role name. One
word per concept.
