---
description: Skills are programs whose I/O boundary is tool calls — mocking that boundary creates controlled environments for testing whether instructions produce correct behavior, complementing text artifact testing with instruction-level regression detection
type: types/note.md
traits: [title-as-claim]
tags: [document-system, constraining, learning-theory]
---

# Unit testing LLM instructions requires mocking the tool boundary

Skills are programs written in natural language and executed by an LLM. Their dependencies — file reads, searches, writes — flow through tool calls. This makes the tool layer the natural seam for dependency injection: replace real tools with mocks that return predetermined data, and you can test the instructions in isolation.

This is the instruction-testing half of the [doubled testing surface](./programming-practices-for-prompts-need-question-specific-evidence.md). The existing [text testing pyramid](./automated-tests-for-text.md) covers artifact testing (is this note good?). Tool mocking covers instruction testing (does this skill reliably produce correct behavior?). These are separate testing targets even with a deterministic generator: one acceptable artifact does not establish reliable generation across inputs. The [governing reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) determines which departures count as conformance failures.

## Architecture

A test fixture has three parts:

1. **Mock KB state** — a small set of fake notes with known relationships, provided as a dictionary of path→content. Five to ten notes suffice for most skill tests.
2. **Mock tool layer** — intercepts tool calls and returns fixture data. `Read` returns predetermined content, `Grep` returns predetermined matches, `Write` captures output for assertion. The fidelity question: mocks can return hardcoded results (fast, brittle) or actually search the fixture data (slower, catches more bugs).
3. **Assertions** — check the captured output (what the skill wrote) and optionally the tool call trace (what the skill did).

For the connect skill, the mock surface is: `Bash` (qmd commands, grep fallback), MCP semantic search tools, `Grep`, `Glob`, `Read` for discovery; `Write` for the connection report output. The Write mock is the primary assertion target — did the report find the expected connections with articulated relationships?

## What assertions look like

Assertions split into two kinds that map to different [oracle strengths](./oracle-strength-spectrum.md):

**Behavioral assertions (hard oracle)** — did the skill follow its protocol?
- Called Read on the target note before searching (correct sequencing)
- No Edit calls made (connect-new is discovery-only)
- Attempted semantic search before falling back to grep
- Checked that candidate paths exist

**Output assertions (soft oracle)** — did the skill produce correct results?
- Report mentions note X as a connection (grep the output)
- Relationship type is specific, not "related" (pattern match)
- No false connections to unrelated fixture notes
- Handles edge cases: reports honestly when no connections exist

The behavioral assertions are cheap and deterministic — ideal for regression testing. The output assertions require either LLM-as-judge or careful fixture design where expected connections are unambiguous enough to check with string matching.

## This is constraining tooling

A test suite for instructions is a [constraining](./definitions/constraining.md) mechanism. Each test constrains the interpretation space by asserting "this instruction, given these inputs, must produce behavior in this range." When an instruction edit or model update causes a test to fail, the failure is visible evidence that the interpretation has shifted — exactly what constraining is designed to detect and prevent.

Instruction tests can run manually or as required gates. [Activation and response](./methodology-enforcement-is-constraining.md) depend on that configuration: a test blocks promotion only when the workflow requires a passing result.

The cost is real — each test execution is an API call — but the alternative is discovering regressions during production use, which is more expensive in both tokens and trust.

## Open questions

- What granularity? Test full skill execution, or test individual phases (discovery, evaluation, output)?
- How to handle indeterminism? Run N times and check pass rate, or design fixtures with such obvious connections that any reasonable execution finds them?
- Should the mock layer be skill-specific or generic? A reusable mock KB runtime vs per-skill test fixtures.
- When is this worth the API cost? Probably after a skill has constrained enough that regressions matter more than rapid iteration.

---

Relevant Notes:

- [Programming practices for prompts need evidence matched to the question](./programming-practices-for-prompts-need-question-specific-evidence.md) — foundation: identifies the doubled testing surface (instruction testing + artifact testing) that this note proposes a concrete mechanism for
- [automated tests for text](./automated-tests-for-text.md) — complements: covers artifact testing (the other half of the doubled surface); this note covers instruction testing
- [constraining](./definitions/constraining.md) — positions: instruction tests are constraining tooling — they constrain the interpretation space by asserting behavioral expectations
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: instruction tests sit on the enforcement gradient between skills (manual invocation) and hooks (automated blocking)
- [oracle strength spectrum](./oracle-strength-spectrum.md) — grounds: behavioral assertions (tool call patterns) are hard-oracle; output assertions (connection quality) are soft-oracle, mirroring the test pyramid split
- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: conformance judgments require a named reference; generator and artifact checks remain distinct
