# Prune Weak Expansions: Prose has no reliable dereference, so a declared fact must be reinforced where it applies

**Target:** `kb/work/agent-note-improvement/case-02-prose-dereference/baseline-working-tree.md`
**Strongest retained claim:** LLM-read prose does not reliably carry declared facts to distant, non-obvious uses, so important facts need local reinforcement while a normalized check prevents drift.

## Core support

- Opening code/prose contrast: establishes why dereference makes single-source declarations safe in codified systems and why prose lacks the same propagation operation.
- `status: seedling` example: gives the note a concrete KB-local case where a declared fact should shape later interpretation.
- Denormalize-copy/normalize-check paragraph: supplies the operational rule and prevents the note from endorsing unchecked duplication.
- Costs section: keeps the recommendation honest by naming bulk, conditional branching, and guard work.
- Scope section: prevents overreach by making reinforcement a gradient across representational form.
- Testing section: marks the empirical weak point and gives a falsifiable ablation.

## Weak expansions

| Location | Problem | Action | Rationale |
|---|---|---|---|
| Opening code claim | "Single-source-of-truth, correct for code" is broader than the argument needs. The proof depends on mechanical dereference, not code as a domain. | compress | Say single-source is safe where declarations mechanically resolve; this avoids counterexamples from prose-like code comments, conventions, or documentation. |
| `status: seedling` consequences | The note lists several consequences of seedling status without distinguishing the fact from derived policy. | compress | Keep the example, but make clear that restating a literal value is easier to check than restating an interpreted consequence. |
| Main denormalization paragraph | The central rule is good, but "restate it there" can sound like every use needs repetition. | compress | Reframe as restating at the nearest reliable control point, often the point of use. |
| Costs: conditional applicability | The paragraph is useful but overlong; it walks through template branching and process constraints in too much detail. | compress | Keep the branching tradeoff. The extra explanation can be shorter because the central note is not about template design. |
| Costs: guard work | Necessary but slightly repetitive after the main check paragraph. | keep | Keep as its own cost because it guards against the false lesson "duplicate freely." |
| Scope | No weak expansion. | keep | This section does the necessary boundary work. |
| Testing section | Strong material, but the heading "the weak point" and first sentence make the note sound less confident than needed. | compress | Keep the ablation and empirical condition; remove self-weakening phrasing. |

## Proposed shape

1. Formal dereference makes single declarations travel.
2. LLM-read prose uses interpretation, not dereference, so declared facts decay with distance and non-obviousness.
3. Reliable prose-facing control often needs reinforcement at the nearest reliable control point.
4. Safe reinforcement denormalizes reader-facing copies but normalizes the check.
5. Costs: bulk, conditional branching, and guard work.
6. Scope by representational form.
7. Falsifiable ablation.

## Candidate splits

- None needed now. The conditional-branching cost could become a future note if enough examples accumulate, but in this draft it is a supporting caveat rather than bloat.

## Net effect

The note becomes harder to attack if it narrows "code vs prose" to "mechanical dereference vs interpretive propagation," separates facts from derived consequences, and tightens the cost and testing sections. The right edit is compression and precision, not splitting. The central claim is already cohesive.
