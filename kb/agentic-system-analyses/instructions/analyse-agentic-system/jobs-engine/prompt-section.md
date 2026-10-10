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

Write the whole member to `output`. Fields your member repeats from other
members, or from `run` for this prompt's variables of the same name, must equal
them exactly: {identity}. Your citations may resolve
only in these members: {cites}.

[verifies]
You verify {verifies}; the verification type says how a blocker names the
member it addresses.

[refusal]
`refusal` is supplied: correct it under the worker rules.

[output-answers]
Write your answers to the refusal's Blockers to `output-answers`, in the
records contract's grammar.

Before returning, run
`{command-path}/commonplace-validate {output} --artifact {artifact} --role {role}`
as written, and repair findings until it passes. Return one line naming the
files you wrote, or `problem`, without summarizing them.
