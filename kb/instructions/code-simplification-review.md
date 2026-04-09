---
description: Simplification-focused review of Commonplace Python modules. Reads target modules with relevant in-repo dependencies, writes per-module findings in the code-simplification workshop, and summarizes cross-module deletion and consolidation candidates.
type: note
---

# Code simplification review

Use this instruction when reviewing `src/commonplace/` for deletions, helper consolidation, and interface tightening. The goal is not a general bug hunt. The goal is to remove code, collapse duplicate concepts, and make package-era simplifications explicit.

## Inputs

- `{module-paths}` — one or more repo-relative Python module paths under `src/commonplace/`
- optional scope hint — a package slice such as `src/commonplace/cli/` or `src/commonplace/review/`

## Output paths

Write findings under `kb/work/code-simplification/code-reviews/`.

Per-module report path mapping:

1. Start from the repo-relative module path
2. Drop the leading `src/`
3. Drop the trailing `.py`
4. Replace `/` with `--`
5. Prefix with `simplify-` and suffix with `.md`

Example:

- `src/commonplace/cli/validate_notes.py` -> `kb/work/code-simplification/code-reviews/simplify-commonplace--cli--validate_notes.md`

Write the cross-module synthesis to:

- `kb/work/code-simplification/code-reviews/summary.md`

Create `kb/work/code-simplification/code-reviews/` if it does not exist.

## Procedure

### 1. Define scope

Resolve the explicit module list first. If the user gave a directory or package slice rather than files, enumerate the `.py` files under that slice and exclude:

- `__init__.py` files with no substantive logic
- generated assets
- package-data files that are not executable Python modules

### 2. Launch per-module reviews

Spawn one subagent per module in scope. Batch only when a set of tiny leaf modules would otherwise produce mostly empty reports.

Give each subagent:

- the target `{module-path}`
- the mapped `{report-path}`
- the prompt below

## Subagent prompt

Review `{module-path}` for simplification opportunities in Commonplace.

### Context gathering

1. Read the target module in full.
2. Identify imports that resolve within this repo:
   - absolute imports under `commonplace.*`
   - relative imports that resolve to modules under `src/commonplace/`
3. Read relevant parts of those internal dependencies for context.
4. If you suspect flexibility is unused, verify with direct call-site search and relevant tests under `test/commonplace/` before claiming it is dead.

Focus analysis on the target module, but use imported code to spot simplifications: duplicate logic, underused abstractions, replaceable inline code, and places where package-local helpers should absorb command-local logic. Proposed changes may span multiple files if warranted.

### Simplification lenses

Analyze for:

1. **Redundant validation** — checks already guaranteed by shared helpers, upstream parsing, schema validation, or dependency contracts.
2. **Unused flexibility** — options, branches, adapter layers, or legacy packaging assumptions that no current caller exercises.
3. **Redundant parameters** — values that are derivable from other arguments, context objects, or already-resolved paths.
4. **Duplicated derived values** — the same stripped body, parsed frontmatter, resolved gate list, slug, SHA, or path normalization computed in multiple places.
5. **Over-specified interfaces** — functions that pass multiple primitives where one `Path`, dataclass, or existing object would make illegal states impossible.
6. **Reorder operations** — resolve paths, note metadata, gates, or DB state before guards when the resolved value is needed anyway; simplify both branching and later logic.
7. **Local helper duplication** — command-local parsing, markdown handling, or path logic that should route through `commonplace.lib` or an existing `commonplace.review` helper.

Prioritize: remove code, reduce concept duplication, make bugs impossible.

### Commonplace-specific attention points

Look especially for:

- frontmatter parsing or stripping outside `commonplace.lib.frontmatter` and `commonplace.lib.note_parser`
- markdown title or link extraction duplicated outside shared helpers
- repo-root, note-path, or gate-path conventions redefined in multiple modules
- review-system helpers that recompute note SHA, gate SHA, or provenance after another layer already did the work
- compatibility scaffolding that only existed before the package transition to `src/commonplace/`

### Output format

Write findings to `{report-path}` using this shape:

```markdown
# Simplification Review: {module-path}

## Findings

- Severity: high|medium|low
  Candidate: short label
  Why: what can be deleted, collapsed, or tightened
  Evidence: file references and the specific duplicate or redundant concept
  Change shape: the smallest credible simplification

## No-change calls

- Patterns you inspected that look intentionally local or justified

## Dependencies read

- internal modules read for context
```

If there are no worthwhile findings, say so explicitly and still fill `Dependencies read`.

### 3. Synthesize across modules

After the subagents finish:

1. Read all per-module reports.
2. Group repeated themes: duplicated parsing, stale compatibility surface, over-generalized interfaces, repeated filesystem conventions, repeated review-state derivations.
3. Prioritize candidates by deletion payoff and blast radius.
4. Write `kb/work/code-simplification/code-reviews/summary.md`.

The summary should include:

- highest-value simplifications first
- which findings require coordinated multi-file edits
- which findings are safe local deletions
- themes that suggest a new shared helper belongs in `commonplace.lib` or `commonplace.review`
- any claims you rejected because tests or call sites showed the flexibility is real

## Checklist

- [ ] Spawn a subagent per module in scope, batching only when the modules are tiny
- [ ] Each subagent writes findings to the mapped `kb/work/code-simplification/code-reviews/simplify-*.md` file
- [ ] Main agent writes `kb/work/code-simplification/code-reviews/summary.md` with prioritized candidates and repeated themes

## Do not

- Do not treat stdlib or third-party imports as rewrite targets unless they make project-local code redundant.
- Do not propose new abstraction layers unless they delete more complexity than they add.
- Do not call something unused without checking call sites and relevant tests.
- Do not spread the review into unrelated architecture debates. Keep the output tied to concrete simplifications in the chosen modules.
