---
description: "A concept has one word, spelled per surface by a fixed rule: spaced in prose, snake_case in Python, kebab-case in YAML keys, prompt lines, files and commands; code is renamed first when they disagree"
type: reference/types/adr.md
status: accepted
---

# 116 — One word per concept across prose and code

**Status:** accepted
**Date:** 2026-10-10
**Amends:** [ADR 022](./022-active-vocabulary-and-write-path-first-mentions.md): the one-term rule reaches past prose to every surface a concept has in code and declarations.

## Context

ADR 022 and the root instruction file fix one term per concept for prose.
The engine and the analysis gave the same concepts other surfaces: Python
identifiers, plan keys, prompt lines, file and role names, relation tokens
and command names. Nothing said how a word crosses from one surface to
another, so each surface named things on its own. Within a week of the
engine's adoption the glossary needed two columns, "Word" and "API name",
to map prose to code; `set` and `artifact` named one thing; `reasons` in
code wrote `## Findings` in documents; the plan file mixed `max_attempts`
with `verified-by`; and `worker-runtime` sat one qualifier from `runtime`,
the analysed system's runtime, in every worker's prompt. The naming review
of 2026-10-09 found these by applying McConnell's and Martin's naming
rules by hand, and found no place where the rules were recorded, so the
next round of names would drift the same way.

The force that recurs: a decision recorded only in an ADR is read when a
problem is already visible or a deep design is under way, not while an
author names a variable, a key or a file. A naming rule that lives only
here is inert on the day it matters.

## Decision

A concept has one word. Each surface spells that word by a fixed
transformation and introduces no second word:

| Surface | Spelling | "max attempts" |
|---|---|---|
| prose | spaced | max attempts |
| Python identifier | snake_case | `max_attempts` |
| YAML key, prompt line, command, file and role name | kebab-case | `max-attempts` |
| relation token | words joined by colons | `memory:cites:runtime` |

When surfaces disagree, code is renamed first and prose follows, unless
the code's word is the better one, in which case prose adopts it. A word
belongs to the problem domain before the solution domain, and within the
solution domain to the engine before its consumers: the analysed system's
`source` keeps that word, and the engine's input origin yields. A
qualified name is the qualified concept, so `report-verification` is a
verification of the reports and `worker-runtime` was not a runtime. A
surface that cannot spell the word, such as a Python keyword, records the
nearest spelling as an exception, once, where the word is defined.

The engine's and the analysis's words are registered in one place: the
workshop glossary while the workshop is open, then a reference vocabulary
page it extracts into at closure. The register lists the word and its
definition; the API column goes, since the identifier is derivable from
the word. [ADR 113](./113-artifact-runs-execute-declared-plans-with-pinned-judgments.md)'s
word list is the seed of that page.

## Considered alternatives

**Two vocabularies joined by a glossary table.** The state before this
decision. It drifted within a week because the table is consulted after a
name exists, not while it is chosen, and nothing fails when it is wrong.

**Free naming per author with review catching collisions.** What
produced `set` beside `artifact` and `reasons` beside findings. Review
reads one file at a time; a collision spans two.

**YAML keys as Python identifiers, underscores everywhere.** Half the
plan file did this. Rejected because the keys are data read by authors
and workers, the kebab-case convention already held for prompt lines,
file names and commands, and one rule per surface is simpler than one
rule per key.

**A per-surface style guide without the one-word rule.** Style guides
settle case and separators, which is the easy half. The drift came from
second words, which a style guide permits.

## Consequences

Operativity, the part this decision exists for. The rule reaches authors
through channels that are loaded or run during ordinary work, not through
this file:

- **The root instruction file** carries the rule in two lines beside the
  one-term line, with binding force in every session, and names this ADR
  for the reasoning.
- **The plan loader** rejects a plan key or input name containing an
  underscore, so a plan in the wrong spelling fails at start rather than
  being read.
- **A test** keeps the registered words and their identifiers in step: for
  each registered word with a code surface, the transformation of the word
  equals the identifier found in the package, without hardcoding the
  list's size. A new identifier that is a second
  word for a registered concept fails there.
- **Commit messages** for a rename cite the rule they apply, so `git log`
  answers "why this name" without the review, which leaves the frontier
  with its workshop.

Easier: a name is chosen once, in prose, and every surface follows; the
glossary loses a column; a reader of a prompt, a plan and the engine's
code meets one word for one thing. Harder: an existing name that breaks
the rule is a change across every surface at once, with relocation tools
for files and a commit per renamed file; the naming review lists the
first such set.

This decision covers the engine, its reuse modules, the analysis consumer
and the plans and prompts they produce. It has not been applied to the
older command-line tools, the review system or the validator's internals,
whose names predate it; a collision found there is fixed under this rule
when the code is next touched, not by a sweep. Deterministic enforcement
covers spelling and registered words only; that a new word is the right
word is still a judgment.
