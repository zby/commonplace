# Towers of Hanoi — OpenProse Bookkeeping Stress Test

## Hypothesis

The [specification-level separation note](../../kb/notes/specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) predicts that OpenProse-like DSLs recover **scoping** benefits but not **error-correction** benefits. Towers of Hanoi is a pure bookkeeping task — the semantic content is trivial (move a disk) but the recursive structure demands exact tracking of:

1. **Call stack depth and scope** — which recursive call are we in?
2. **Arithmetic conditions** — is n == 1? What is n - 1?
3. **Peg-role permutation** — source/target/auxiliary swap at each level
4. **Move ordering** — 2^n - 1 moves in one exact correct sequence

All of these are operations that a symbolic executor handles trivially (discrete state, deterministic transitions) but that the LLM-as-VM must perform on the stochastic substrate.

## What to observe

- **Move count**: 4 disks → exactly 15 moves. Any other number = bookkeeping error.
- **Move order**: The canonical sequence is deterministic. Any reordering = state tracking failure.
- **Peg confusion**: The source/target/auxiliary roles swap at each recursion level. Getting these wrong is the classic LLM variable-tracking failure.
- **Depth errors**: Failing to recurse to the right depth, or evaluating the base case condition wrong.

## Running

```bash
prose run hanoi.prose
```

Or with in-context state for simpler programs:
```bash
prose run hanoi.prose --in-context
```

## Expected correct output

The 15 moves for `hanoi(4, A, C, B)`:

```
 1. disk 1: A → B
 2. disk 2: A → C
 3. disk 1: B → C
 4. disk 3: A → B
 5. disk 1: C → A
 6. disk 2: C → B
 7. disk 1: A → B
 8. disk 4: A → C
 9. disk 1: B → C
10. disk 2: B → A
11. disk 1: C → A
12. disk 3: B → C
13. disk 1: A → B
14. disk 2: A → C
15. disk 1: B → C
```

## Variations to try

- **3 disks** (7 moves) — easier baseline
- **5 disks** (31 moves) — harder, more chance for error accumulation
- **Track error rate** — run multiple times, count deviations from correct sequence
