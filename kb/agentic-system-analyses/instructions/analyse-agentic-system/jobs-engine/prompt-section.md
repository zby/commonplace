---
description: "The prompt section every analysis worker receives: the member it writes, the types that govern it, and how it corrects, checks and returns"
type: types/instruction.md
---

You write the `{role}` member of this agentic-system analysis. `member-type`
governs that member and wins over the job instruction where they differ;
`worker-rules` governs how you work. Each member you read comes with its type
as `<role>-type`, and the job instruction says what this member must
establish.

This prompt is your complete write procedure. The repository's authoring
skills (`cp-skill-write`, `cp-skill-connect`, `cp-skill-ingest` and the like)
assume an operator, the KB as evidence and KB destinations; do not use them
for this work.

Write the whole member to `output`.

[refusal]
Repair the Findings of `refusal` against frozen evidence, with your previous
output as the baseline.

[output-answers]
Answer the refusal's Blockers in `output-answers`, one `- corrected:` or
`- declined:` entry per blocker in order, under the worker rules' correction
protocol. Write an empty file when no refusal is supplied or its Blockers are
`none`.

Before returning, run
`{command-path}/commonplace-validate {output} --artifact {artifact} --role {role}`
as written, and repair findings until it passes. A pass
establishes form and quotation occurrence, not acceptance: code checks
identity and frozen sources, and an independent verifier judges support.
Return one line naming the files you wrote, or `problem`.
