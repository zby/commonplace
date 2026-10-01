# Draft intent paragraphs for the three analysts

- **Commissioned:** 2026-10-01, by the operator, after a review of the [balanced compaction plan](./balanced-compaction-plan.md).
- **Purpose:** the plan's runtime, memory and epistemic candidates let the worker choose investigation order and depth, but state only what to write. A worker needs the purpose of the result to choose by. Each paragraph below states what the member is for, who relies on it, and which errors make it useless.
- **Status:** draft for the operator's correction. No live instruction or candidate is changed. The purposes are an agent's reading of the contracts and consumers, not the operator's stated intent.
- **Placement:** in each candidate, as the first paragraph under `## Mission and discretion`, before the sentence that grants discretion.

## Runtime analyst

```markdown
This member is the account of how the system actually runs: what decides
the next step, what each model call receives, and which state and actions
lie outside the call. The memory and epistemic analysts start from it and
no job rewrites it, so a route missing here is likely to be missing from
the whole analysis. It also bounds the system's claims: a reader should
learn which guarantees hold on every path that can do the claimed work, and
which hold only on the path the documentation describes. Spend effort where
a wrong answer would change that judgment. A full feature inventory is not
the goal; a guarantee reported without its uncovered paths is the costly
error.
```

## Memory analyst

```markdown
This report answers what the system retains through use, how that material
returns to a later model call, and whether anything shows that it changes
behavior. Storage alone is rarely the interesting part; what is read back,
when, and with what force is. A later cross-system synthesis reads the
comparison profile first, beside the profiles of other systems and without
this report's prose. Each value must therefore mean here what its
definition says everywhere, and must rest on a record. An overstated value
damages that comparison more than an honest `partial` or `uninspected`.
Spend effort on the mechanisms that distinguish this system from a plain
store, and keep thin areas short and explicitly limited.
```

## Epistemic analyst

```markdown
This member lets a reader decide how far to rely on what the system
produces or retains. It separates content the system only stores or passes
on from content it derives or conjectures, and it shows which checks stand
between that content and later behavior, and what each check licenses.
Systems often describe retention or reshaping as learning or knowledge;
the member tests such claims against the routes that exist. Two errors make
it useless: granting warrant that no check supplies, and reporting a
system-wide absence from a branch that was not inspected. A finding that
the system stores and serves, and nothing more, is a complete result. Do
not look for epistemic structure the system neither claims nor has.
```

## Cost

| Paragraph | Bytes |
|---|---:|
| Runtime | 673 |
| Memory | 713 |
| Epistemic | 720 |

Against the plan's savings, the runtime candidate would grow by about 365 bytes over the live job (308 saved, 673 added). The memory candidate would still save about 90, and the epistemic candidate about 500. With these paragraphs the three changes are no longer a compression; their case rests on analysis quality.

## Basis for each statement, and what is uncertain

- **Runtime as the baseline nobody rewrites:** `jobs/runtime.md` and the runtime type. The three-way separation (next step, per-call context, external state and action) is the claim of the note the skill cites for the runtime job.
- **Runtime's second use, bounding claims:** inferred from the job's alternate-path and guarantee steps. The operator has not said that this is the primary value of the runtime member.
- **Memory's question:** the two notes the skill cites for the memory analyst, on memory as storage, activation and learning, and on storage not implying activation.
- **Memory's reader:** `synthesize-agent-memory-landscape` builds a matrix from the profiles. That it reads the profile "first" is accurate for the matrix step; it later reads the mechanisms too.
- **Epistemic's purpose:** the epistemic type's definition of its question, and its early branch for storage-only systems. "Lets a reader decide how far to rely" is an inference; the type states the question, not the reader's decision.
- **Not stated in any paragraph:** the research use of these analyses as evidence about theory builders. If that is a purpose the analysts should serve, the runtime or epistemic paragraph needs a sentence for it.
