# Gate review: semantic/completeness-boundary-cases

## completeness-A
### Findings
- INFO: The concrete workflow's step 2-4 dichotomy ("is there a deterministic rule that would have caught this? If yes → codify; if no → regression test") is logically exhaustive by construction, but boundary cases sit between the branches: a rule that would have caught only *part* of a failure cluster, or a rule that exists but is too brittle/expensive to deploy. Coverage is possible but strained — the "no" branch's "partial codification" gesture absorbs these only loosely. The note makes no exhaustiveness claim for the pattern itself ("One answer: you mine them"), so nothing falls outside claimed coverage.
## Result: PASS

## completeness-B
### Findings
- WARN: The note claims "These four surfaces are the only routes through which instructions can reach an agent's context — every instruction the agent ever sees arrives through one of them." Boundary cases break this: (1) the user's own message — the most common instruction route of all — is none of the four surfaces; (2) the harness system prompt (tool definitions, environment info) carries instructions and is not CLAUDE.md, a skill description, a skill body, or a task doc; (3) hook-injected output and system reminders inject instructions mid-session outside all four; (4) MCP tool descriptions are an always-loaded instruction surface distinct from skill descriptions. These clearly fall outside the claimed coverage. The hierarchy itself is useful without the totality claim — scope clarification ("the repo-authored instruction surfaces") is the cheaper fix over expanding the enumeration.
## Result: WARN

## completeness-C
### Findings
- WARN: The note claims "This exhausts the space — every LLM output an operator chooses to keep falls into one of four artifact classes" (code, documents, configuration, accumulated logs). Boundary cases break the exhaustiveness: (1) kept multimodal outputs — generated images or diagrams-as-renderings — fit none of the four classes cleanly; (2) generated synthetic datasets (e.g. a CSV of test fixtures) are not documents, config, or logs, and only strainedly "code"; (3) a kept LLM-generated *prompt* sits between code and configuration with no clean home; (4) a saved conversation transcript sits between "document" and "accumulated log" — between enumerated items rather than in one. The four classes are fine as illustrative breadth; the "exhausts the space" claim is what fails. Dropping the exhaustiveness sentence (as scope clarification) is a better fix than adding classes.
## Result: WARN

## completeness-D
### Findings
- INFO: The two-strategy framing ("There are two strategies for getting reliable output from a generator whose outputs vary") is stated without an exclusivity claim, but boundary cases are strained: self-consistency/majority voting aggregates samples rather than filtering or constraining, and iterative refinement (verify-then-regenerate loops) combines both poles rather than mapping to one. Since the note does not claim the pair exhausts all reliability techniques, these are strained mappings, not coverage violations.
- INFO: The four artifact classes are introduced with "This applies broadly:" — explicitly illustrative, not a coverage claim — so cases like generated images or synthetic datasets falling outside the list do not violate anything the note asserts.
## Result: PASS

## completeness-E
### Findings
- WARN: The note claims "Every instruction falls into exactly one of two classes: universal rules, which load always, and task-specific rules, which load only when doing that task." The partition breaks on the note's own hierarchy: skill *descriptions* (surface 2) are task-specific instructions ("invoke this when doing X") that load always — a case squarely between the two classes, violating "exactly one." Other boundary cases: mid-frequency instructions (git commit rules apply only during commits yet the note places them in always-loaded CLAUDE.md as "universal"), and routing-table entries, which are task-specific pointers loaded every session. The two-class partition is cleaner than the reality the note itself describes; the earlier softer phrasing ("universal rules load always, task-specific rules load when doing that task" as a design principle, not a partition of all instructions) covered the space without the false dichotomy.
## Result: WARN

## completeness-F
### Findings
- WARN: The note claims "There are only two strategies... every reliability technique reduces to one of them" (constrain the generator / filter the samples). Boundary cases fall outside: (1) post-hoc repair — editing or auto-fixing a flawed output — neither constrains the generator nor rejects the sample; it transforms the sample, a third move; (2) self-consistency/majority voting aggregates across samples into a new output that no single run produced — not filtering as defined ("rejects the failures") and not generator-side; (3) iterative refinement loops (verifier feedback fed back into regeneration) reduce at best to a *combination* of both, which contradicts "reduces to one of them." Strategy 1 is defined as "tighter prompts, more examples, lower temperature," so even fine-tuning maps only strainedly. The dichotomy is a useful lens; the "only two / every technique reduces" claim is what breaks. Softening the claim is the lighter fix than expanding the taxonomy.
## Result: WARN
