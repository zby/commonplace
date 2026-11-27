# Note extraction trials

Operator commission, 2026-11-25: try the opt-in [note extraction instruction](../experimental-mutations/check-what-a-note-extraction-adds.md) on historical cases and report what changes. The deliverable is a paired comparison, not a library edit or adoption decision. Close after reporting; retain useful observations for the mutation workshop.

Completed: [results and next candidate comparison](./results.md).

## Cases and assignments (fixed before launch)

Four fresh project workers, same inherited model and effort, one draft per condition. Within each pair only the instruction changes. Each reads the specified pre-extraction blobs, not the historical extraction or subsequent evidence. Isolation is by fresh conversation and explicit input restrictions, not a filesystem sandbox.

| Case | Historical inputs | Ordinary extraction | With instruction |
|---|---|---|---|
| A: extract the shared Bitter Lesson argument | `778d091da7dadf1aeebcb9ec70ee2b5165b7cf11`: `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md`, `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md` | drafts/A1.md | drafts/A2.md |
| B: extract the partial-evaluation framing, leaving the parent operational | `dbb48035aafd6cd90acf45055dcec82f294f8abb`: `kb/notes/frontloading-spares-execution-context.md` | drafts/B2.md | drafts/B1.md |

See [assignments](./assignments.md) for exact commissions. [Instruction as tested](./instruction-as-tested.md), SHA-256: `ee0e3bddf89b7125870d98c73ef72115c58411b268c8d19c6d521a778b1c0bca`.

## Comparison

Read the two notes and their proposed citation sentences against the source. For A: distinguish classification as search from evidence of successful generalization; preserve the open question about retention at scale. For B: check whether the settled analogy and its limits travel with the argument, without inflating the claim or changing its purpose. In both: identify concrete gains, losses and equivalent outcomes; don't count restating the instruction as success. Judge the text, not unobserved effort. No model ranking or success-rate inference from one pair per case. The historical edits are comparisons, not answer keys; later evidence is not available to writers.
